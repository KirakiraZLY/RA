import torch
import pyro
import pyro.distributions as dist
from pyro.infer import SVI, Trace_ELBO, Predictive
from pyro.optim import Adam

# 数据准备
torch.manual_seed(42)
X = torch.randn(100, 20)  # 100个样本，20个基因
Y = torch.randn(100)

# 模型定义
def model(X, Y):
    weight_prior = dist.Normal(0, 1).expand([X.shape[1]]).to_event(1)
    weights = pyro.sample("weights", weight_prior)
    prediction = X.matmul(weights)
    with pyro.plate("data", size=len(Y)):
        pyro.sample("obs", dist.Normal(prediction, 1), obs=Y)

# 推断算法
def guide(X, Y):
    weight_loc = torch.randn(X.shape[1])
    weight_scale = torch.randn(X.shape[1]).abs()
    weights = pyro.sample("weights", dist.Normal(weight_loc, weight_scale).to_event(1))

# SVI引擎
adam_params = {"lr": 0.01}
optimizer = Adam(adam_params)
svi = SVI(model, guide, optimizer, loss=Trace_ELBO())

# 训练模型
num_iterations = 1000
for step in range(num_iterations):
    elbo = svi.step(X, Y)
    if step % 100 == 0:
        print(f"Step {step}/{num_iterations}, ELBO: {elbo}")

# 获取后验分布的样本
predictive = Predictive(model, guide=guide, num_samples=1000, return_sites=("weights", "obs"))
posterior_samples = predictive(X, Y)

# 根据后验分布进行预测
def predict(X, posterior_samples):
    weights_samples = posterior_samples["weights"].mean(dim=0)
    predictions = X.matmul(weights_samples.t())
    return predictions

# 在测试数据上进行预测
X_test = torch.randn(10, 20)  # 10个测试样本，20个基因
predictions = predict(X_test, posterior_samples)

# 打印预测结果
print("Predictions:", predictions)

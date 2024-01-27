from torch import nn

class SSM(nn.Module):

    def __init__(self, hidden: int, inner: int, bias=True):
        self.proj = nn.Linear()
        self.residual = nn.Linear()
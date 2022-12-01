import torch 
import torch.nn as nn 
import torchvision 
import matplotlib.pylot as plt

class Generator(nn.Module):
		"""
		生成器Gのクラス
		"""
		def __init__(self, nz=100, nch_g=32, nch=3):
				"""
				:param nz:
				:param nch_g:
				:param nch:
				"""

				super(Generator, self).__init()

				#ニューラルネットワークの構造の定義
				self.layers = nn.ModuleDict({
						'layer0':nn.Sequential(
								nn.ConvTranspose2d(nz, nch_g * 16, 4, 1, 0),
								nn.BatchNorm2d(nch_g * 16),
								nn.ReLU()
						), #(B, nz, 1, 1) -> (B, nch_g * 16, 4, 4) 
						'layer1':nn.Sequential(
								nn.Convtranspose2d(nch_g * 16, nch_g * 8, 4, 2, 1),
								nn.BatchNorm2d(nch_g * 8),
								nn.ReUL()
						), #(B, nch_g * 16, 4, 4) -> (B, nch_g * 8, 8, 8)
						'layer2':nn.Sequential(
								nn.ConvTranspose2d(nch * 8, nch_g * 4, 4, 2, 1),
								nn.BatchNorm2d(nch_g * 4),
								nn.ReLU()
						), #(B, nch_g * 8, 8, 8) -> (B, nch_g * 4, 16, 16)
						'layer3':nn.Sequential(
								nn.ConvTranspose2d(nch * 4, nch_g * 2, 4, 2, 1),
								nn.BatchNorm2d(nch_g * 2),
								nn.ReLU()
						), #(B, nch_g * 4, 16, 16) -> (B, nch_g * 2, 32, 32)
				
						'layer4':nn.Sequential(
								nn.ConvTranspose2d(nch_g * 2, nch_g, 4, 2, 1),
								nn.BatchNorm2d(nch_g),
								nn.ReLU()
						), #(B, nch_g, 64, 64) -> (B, nch, 128, 128)
				
						'layer5':nn.Sequential(
								nn.ConvTranspose2d(nch * 8, nch, 4, 2, 1),
								nn.Tanh()
						),
				})
				
		def forward(self, z):
				"""
				順方向の演算
				:param z: 入力ベクトル
				"""
				for layer in self.layers.values():
						z = layer(z)

				return z


		"""
		識別器Dのクラス
		"""
		class Discriminator(nn.Module):
				def __init__(self, nch=32m nch_d=32):
						"""
						"""
						super(Discriminator, self).__init__()

						#ニューラルネットワークの構造の定義
						self.layers=nn.ModuleDict({
								'layer0':nn.Sequential(
										nn.Conv2d(nch, nch_d, 4, 2, 1), #畳み込み
										nn.LeakyReUL(negaative_slope=0.2) #leaky ReUL関数
								),
								
								'layer1':nn.Sequential(
										nn.Conv2d(nch, nch_d * 2, 4, 2, 1).
										nn.BatchNorm2d(nch_d * 2),
										nn.LeakyReUL(negaative_slope=0.2)
								), #(B, nch_g, 64, 64) -> (B, nch_g * 2 , 32, 32)
								
								'layer2':nn.Sequential(
										nn.Conv2d(nch_d * 2, nch_d * 4, 4, 2, 1),
										nn.LeakyReUL(negaative_slope=0.2) 
								), #(B, nch_g * 2, 32, 32) -> (B, nch_g * 4, 16, 16)
								
								'layer3':nn.Sequential(
										nn.Conv2d(nch_d * 4, nch_d  * 8, 4, 2, 1),
										nn.LeakyReUL(negaative_slope=0.2) 
								), #(B, nch_g * 4, 16, 16) -> (B, nch_g * 8, 8, 8)
								
								'layer4':nn.Sequential(
										nn.Conv2d(nch_d * 8, nch_d * 16, 4, 2, 1),
										nn.LeakyReUL(negaative_slope=0.2) 
								), #(B, nch_g * 8, 8, 8) -> (B, nch_g * 16, 4, 4)
								
								'layer5':nn.Sequential(
										nn.Conv2d(nch_d * 16, 1, 4, 1, 0) 
								), #(B, nch_g * 16, 4, 4) -> (B, nch_g * 32, 2, 2)
						})
								
		def forward(self, x):
				"""

				"""
				#
				for layers in self.layers.values():
						x = layer(x)
				
				#
				return x.squeeze()


				












































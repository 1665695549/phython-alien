print("Hello Python world")

	def prep_high_score(self):
		"""将最高得分转换为渲染的图像"""
		high_score=int(round(self.stats.high_score,-1)
		#high_score_str = "{:,}".format(high_score)
		self.high_score_image=self.font.render(str(self.stats.high_score),True,self.text_color,self.ai_settings.bg_color)
		#将最高得分放在屏幕顶部中央
		self.high_score_rect=self.high_score_image.get_rect()
		self.high_score_rect.centerx=self.screen_rect.centerx
		self.high_score_rect.top=self.score_rect.top

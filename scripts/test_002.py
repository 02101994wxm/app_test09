import allure

class Test_002:
    def test_png(self):
        with open("C:\\Users\\Ming123\\Desktop\\APP07\\Scripts\\123.png", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)


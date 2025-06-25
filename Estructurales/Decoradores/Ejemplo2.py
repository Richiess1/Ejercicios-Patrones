class TextComponent:
    def render(self):
        pass


class PlainText(TextComponent):
    def __init__(self, text):
        self.text = text

    def render(self):
        print(f"[PlainText] Original text: {self.text}")
        return self.text


class ItalicDecorator(TextComponent):
    def __init__(self, component):
        self.component = component

    def render(self):
        result = self.component.render()
        wrapped = f"<i>{result}</i>"
        print(f"[ItalicDecorator] Applied italic: {wrapped}")
        return wrapped


class BoldDecorator(TextComponent):
    def __init__(self, component):
        self.component = component

    def render(self):
        result = self.component.render()
        wrapped = f"<b>{result}</b>"
        print(f"[BoldDecorator] Applied bold: {wrapped}")
        return wrapped


class Heading2Decorator(TextComponent):
    def __init__(self, component):
        self.component = component

    def render(self):
        result = self.component.render()
        wrapped = f"<h2>{result}</h2>"
        print(f"[Heading2Decorator] Applied heading level 2: {wrapped}")
        return wrapped

if __name__ == "__main__":
    text = PlainText("Welcome to the WYSIWYG editor")
    formatted_text = Heading2Decorator(BoldDecorator(ItalicDecorator(text)))
    final_result = formatted_text.render()

    print("\n[Final Result]")
    print(final_result)
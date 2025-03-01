"""
  def yield | (): construct to create generator object
"""

def generate():
    num = 0
    yield num
    num += 1


if __name__ == "__main__":
    for v in range(10):
        print(next(generate()))

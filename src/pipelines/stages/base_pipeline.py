class BasePipeline:

    def __init__(self):

        self.stages = []

    def run(self, context: dict):

        for stage in self.stages:

            print(f"Executing stage: {stage.name}")

            context = stage.execute(context)

        return context
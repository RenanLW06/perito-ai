class BasePipeline:

    def __init__(self):

        self.stages = []

    def run(self, context):

        for stage in self.stages:

            context.set_stage(stage.name)

            context.add_log(f"Executing {stage.name}")

            stage.execute(context)

        return context
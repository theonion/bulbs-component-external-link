
class PipelineWrapper(object):

    def __init__(self):
        self.name = ""
        self.dict = {
            "source_filenames": (),
            "output_filename": ""
        }

    def set_name(self, name):
        self.name = name
        return self

    def add_source_filename(self, filename):
        self.dict["source_filenames"] += (filename,)
        return self

    def set_output_filename(self, filename):
        self.dict["output_filename"] = filename
        return self

    def update_pipeline(self, pipeline_config):
        pipeline_config.update({self.name: self.dict})
        return self


cms_js = PipelineWrapper()
cms_js \
    .set_name("external_link_cms") \
    .set_output_filename("js/external-link-cms.js") \
    .add_source_filename("cms/external-link/*.js")

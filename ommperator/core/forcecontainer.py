class ForceContainer(list):
    """ A force container is a container that holds ForceOmmperators.
    It facilitaties mass-modifying properties"""
    def update(self, **kwargs):
        for force_ommp in self:
            force_ommp.set_params(**kwargs)


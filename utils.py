class ActiveTabMixin(object):
    active_tab = 'home'

    def get_context_data(self, *args, **kw):
        ctx = super(ActiveTabMixin, self).get_context_data(*args, **kw)
        ctx.update({'active_tab': self.active_tab})
        return ctx
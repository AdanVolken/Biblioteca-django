class BibliotecaRouter(object):

    router_apps_label = {'auth', 'contenttypes', 'sessions', 'admin', 'biblioteca',}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.router_apps_label:
            return 'default'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.router_apps_label:
            return 'default'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if(
            obj1._meta.app_label in self.router_apps_label or
            obj2._meta.app_label in self.router_apps_label
        ):
            return True
        return False
    
    def allow_migrate(self, db , app_label, model_name = None, **hints):
        if app_label in self.router_apps_label:
            return db == 'default'
        return None
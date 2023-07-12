from bitfield.types import BitHandler


def get_selected_labels(self):
    return (self.get_label(k) for k in self._keys if getattr(self, k).is_set)


BitHandler.get_selected_labels = get_selected_labels

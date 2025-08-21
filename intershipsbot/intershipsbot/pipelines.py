import re

class CleanTextPipeline:
    def process_item(self, item, spider):
        for field, value in item.items():
            if isinstance(value, str):
                # Strip leading/trailing spaces & newlines
                cleaned = value.strip()
                # Replace multiple spaces/newlines/tabs with a single space
                cleaned = re.sub(r'\s+', ' ', cleaned)
                item[field] = cleaned
            elif isinstance(value, list):
                # Clean lists of strings
                cleaned_list = []
                for v in value:
                    if isinstance(v, str):
                        cleaned = v.strip()
                        cleaned = re.sub(r'\s+', ' ', cleaned)
                        cleaned_list.append(cleaned)
                    else:
                        cleaned_list.append(v)
                item[field] = cleaned_list
        return item

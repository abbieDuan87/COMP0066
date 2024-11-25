import datetime as dt

class JournalEntry:
    def __init__(self, title, entry, date, time):
        self.title = title
        self.entry = entry
        self.date = date
        self.time = time

    def get_title(self):
        return self.title
    
    def get_entry(self):
        return self.entry
    
    def get_date(self):
        return self.date

    def get_time(self):
        return self.time  
      
    def to_dict(self):
        datetime = dt.datetime.combine(self.date, self.time)
        return {
            'title' : self.title,
            'entry' : self.entry,
            'datetime' : datetime
        }
    
    def strip_entry(self):
        if len(self.entry) > 100:
            stripped_entry = self.entry[:99] + '...'
            return stripped_entry
    
    def __str__(self):
        return (
            f"JournalEntry(\n"
            f"  id={self.title},\n"
            f"  entry={self.entry}"
            f"  date={self.date},\n"
            f"  time={self.time},\n"
            f")"
        )
    
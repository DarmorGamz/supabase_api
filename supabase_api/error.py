class SupabaseApiException(Exception):
    """
    Custom exception class for Supabase errors.
    """
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"SupabaseApiException: {self.message}"

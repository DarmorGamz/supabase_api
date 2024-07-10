import logging
from supabase import create_client, Client
from .error import (SupabaseApiException)

LOGGER = logging.getLogger('supabase_api')

class SupabaseAPI(object):
    """
    blah
    """
    def __init__(self, supabase_url: str, supabase_key):
        if not supabase_url or not supabase_key:
            raise SupabaseApiException("Missing Supabase URL or API key")
            return
        
        self.url = supabase_url
        self.key = supabase_key
        
        try:
            self.sp: Client = create_client(self.url, self.key)
        except Exception as e:
            raise SupabaseApiException(f"Failed to create Supabase client: {str(e)}")

    def add_row(self, table: str, data: dict):
        """
        Adds a row to the specified table.
        
        :param table: The name of the table.
        :param data: A dictionary representing the row to be added.
        """
        response = self.sp.table(table).insert(data).execute()
        if response.status_code == 201:
            print("Row added successfully.")
        else:
            print("Error adding row:", response.data)

    def update_row(self, table: str, row_id: int, data: dict):
        """
        Updates a row in the specified table.
        
        :param table: The name of the table.
        :param row_id: The ID of the row to be updated.
        :param data: A dictionary representing the updated data.
        """
        response = self.sp.table(table).update(data).eq('id', row_id).execute()
        if response.status_code == 200:
            print("Row updated successfully.")
        else:
            print("Error updating row:", response.data)

    def replace_row(self, table: str, row_id: int, data: dict):
        """
        Replaces a row in the specified table.
        
        :param table: The name of the table.
        :param row_id: The ID of the row to be replaced.
        :param data: A dictionary representing the new data.
        """
        # First, delete the existing row
        delete_response = self.sp.table(table).delete().eq('id', row_id).execute()
        if delete_response.status_code == 200:
            # Then, insert the new row
            data['id'] = row_id
            insert_response = self.sp.table(table).insert(data).execute()
            if insert_response.status_code == 201:
                print("Row replaced successfully.")
            else:
                print("Error inserting new row:", insert_response.data)
        else:
            print("Error deleting row:", delete_response.data)
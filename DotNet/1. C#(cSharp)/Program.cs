using System;
using System.Net.Http;
using System.Text;

namespace Hello
{
    public class Program
    {

        static void Test()
        {
            Console.WriteLine("Entering into the API call");

            string url = "https://account.uipath.com/oauth/token";

            // Define the request body
            string requestBody = "{\"grant_type\":\"refresh_token\",\"client_id\":\"8DEv1AMNXczW3y4U15LL3jYf62jK93n5\",\"refresh_token\":\"FIonuqnNUOyQxJyQpqJeQXSi2GYlUH3NkDilcrQ1Z1Eex\"}";

            // Create a new HttpClient instance
            using (HttpClient client = new HttpClient())
            {
                // Define the request content with the JSON body
                StringContent content = new StringContent(requestBody, Encoding.UTF8, "application/json");

                try
                {
                    // Send the POST request and get the response synchronously
                    HttpResponseMessage response = client.PostAsync(url, content).Result;

                    // Log the status code
                    Console.WriteLine($"Status Code: {response.StatusCode}");

                    // Check if the response is successful
                    if (response.IsSuccessStatusCode)
                    {
                        // Read the response content synchronously
                        string responseContent = response.Content.ReadAsStringAsync().Result;
                        
                        // Log the token
                        Console.WriteLine("Token:");
                        Console.WriteLine(responseContent);
                    }
                    else
                    {
                        Console.WriteLine($"Failed to make the API call. Status code: {response.StatusCode}");
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"An error occurred: {ex.Message}");
                }
            }

            Console.WriteLine("Exiting from API Call");
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Hello Rakesh");

            Test();

        }
    }
}

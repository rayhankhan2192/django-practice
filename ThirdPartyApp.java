import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class ThirdPartyApp {
    public static void main(String[] args) {
        try {
            // Define the URL
            String urlString = "http://127.0.0.1:8000/arena/details/";
            URL url = new URL(urlString);

            // Open a connection to the URL
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();

            // Set the request method to GET
            connection.setRequestMethod("GET");

            // Get the response code
            int responseCode = connection.getResponseCode();
            System.out.println("Response Code: " + responseCode);

            // Read the response
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder responseStringBuilder = new StringBuilder();
            String line;

            while ((line = reader.readLine()) != null) {
                responseStringBuilder.append(line);
            }
            reader.close();

            // Print the response
            System.out.println("Response Data: " + responseStringBuilder.toString());

            // Disconnect the connection
            connection.disconnect();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

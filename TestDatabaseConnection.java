import java.sql.Connection;
import java.sql.SQLException;

public class TestDatabaseConnection {
    public static void main(String[] args) {
        try (Connection connection = DatabaseUtil.getConnection()) {
            System.out.println("Connected to the database!");
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

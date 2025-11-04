import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

public class FileCopy {
    public static void main(String[] args) throws Exception {
        if (args.length != 2) {
            System.err.println("Usage: java FileCopy sourceFile destFile");
            System.exit(1);
        }
        Path src = Path.of(args[0]);
        Path dst = Path.of(args[1]);
        Files.copy(src, dst, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Copied " + src + " -> " + dst);
    }
}

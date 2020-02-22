package backend;

import java.io.File;
import gui.gui;

public class Program {
    public static final String version = "1.0.0";
    final String comment = "//Created using ProgramMaker v" + version;

    String code = comment + "\n";
    String path = new String();

    public static void main(String[] args) {
        gui.create();
    }
}

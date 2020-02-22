package gui;

import javax.swing.*;
import backend.Program;

import java.awt.*;

public class gui {
    public static void create() {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                Gui();
            }
        });
    }

    public static void Gui() {
        JFrame frame = new JFrame(String.format("ProgramMaker %s", Program.version));
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        frame.setJMenuBar(menubar.load());

        frame.pack();
        frame.setVisible(true);
    }
}

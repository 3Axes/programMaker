package gui;
import javax.swing.*;
import java.util.ArrayList;

public class menubar {

    static JMenuBar MenuBar = new JMenuBar();
    static ArrayList<ArrayList<String>> items = new ArrayList();

    public static JMenuBar load() {
        pack();
        return MenuBar;
    }

    static void pack() {
        create();
        JMenu[] menuArray = new JMenu[items.size()];
        for (int k = 0; k < items.size(); k++) {
            ArrayList x = items.get(k);
            JMenuItem[] itemArray = new JMenuItem[x.size() - 1];
            for (int i = 1; i < x.size(); i++) {
                itemArray[i - 1] = new JMenuItem((String) x.get(i));
            }

            JMenu menu = new JMenu((String) x.get(0));
            for (JMenuItem item : itemArray) {
                menu.add(item);
            }
            menuArray[k] = menu;
        }

        for (JMenu opt : menuArray) {
            MenuBar.add(opt);
        }
    }

    static void create() {
        //File
        //File > Open
        //File > Save

        ArrayList<String> File = new ArrayList();
        File.add(0, "File");
        File.add(1, "Open");
        File.add(2, "Save");
        items.add(File);
    }
}

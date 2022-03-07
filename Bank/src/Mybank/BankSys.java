package Mybank;

import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JToolBar;
//import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

class BankSystemPvt implements ActionListener{
	RandomAccessFile file;
	DataInputStream din;
	DataOutputStream dout;
	JFrame bank;
	JPanel pnlp;
	
	JLabel lb;
	
	JFrame frmacc;
	JPanel pnlacc;
	JTextField tfacc,tfn,tfb,tft;
	JButton btacc;

	JFrame frmv;
	JPanel pnlv;
	JScrollPane sp;
	JTable tbv;

	JFrame frmd;
	JPanel pnld;
	JButton btd;
	JTextField tfd1,tfd2;
	private JMenu help;
	private JMenuItem about;

	int f=0;
	private JMenuBar mbar;
	private JMenu file1;
	private JMenu transaction;
	private JMenuItem newacc;
	private JMenuItem search;
	private JMenuItem view;
	private JMenuItem exit;
	private JMenuItem withdraw;
	private JMenuItem deposit;
	JToolBar tb;
	JButton newac,searchac,exitac,helpac;

	BankSystemPvt()
	{
		bank=new JFrame("Java Bank software");
		bank.setSize(690,600);
		bank.setVisible(true);
		bank.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		lb=new JLabel();		
		
		mbar=new JMenuBar();
		bank.setJMenuBar(mbar);
		pnlp=new JPanel(new BorderLayout());
	//	bank.add(new JTextArea(34,5),"South");
		bank.setLayout(new BorderLayout());

		file1=new JMenu("File");
		mbar.add(file1);
		newacc=new JMenuItem("NewAccount");
		file1.add(newacc);
		search=new JMenuItem("Search");
		file1.add(search);
		view=new JMenuItem("View");
		file1.add(view);
		exit=new JMenuItem("Exit");
		file1.add(exit);
		transaction=new JMenu("Transaction");
		mbar.add(transaction);
		withdraw=new JMenuItem("Withdraw");
		transaction.add(withdraw);
		deposit=new JMenuItem("Deposit");
		transaction.add(deposit);
		help=new JMenu("Help");
		mbar.add(help);
		about=new JMenuItem("About");
		help.add(about);
		
		tb=new JToolBar();
		
		newac=new JButton(new ImageIcon("E:/imagesimp/new.gif"));
		tb.add(newac);
		searchac=new JButton(new ImageIcon("E:/imagesimp/find.gif"));
		tb.add(searchac);	
		exitac=new JButton(new ImageIcon("E:/images/Keys.gif"));
		tb.add(exitac);	
		helpac=new JButton(new ImageIcon("E:/imagesimp/about.gif"));
		tb.add(helpac);	
		
		bank.add(pnlp,"Center");
		pnlp.add(tb,"North");
		
		newacc.addActionListener(this);
		search.addActionListener(this);
		view.addActionListener(this);
		exit.addActionListener(this);
		withdraw.addActionListener(this);
		deposit.addActionListener(this);
		about.addActionListener(this);
		newac.addActionListener(this);
		searchac.addActionListener(this);
		exitac.addActionListener(this);
		helpac.addActionListener(this);
			
		bank.add(lb,"South");
	}


	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		
		if(e.getSource()==about)
		{

			JOptionPane.showMessageDialog(bank, "Banking System built by java.");
		}
		if(e.getSource()==helpac)
		{

			JOptionPane.showMessageDialog(bank, "Banking System by Mhtonoy.");
		}
		
		if(e.getSource()==newac)
		{
			newAcc();
			//lb.setText("New Account Registration is Going on...");
		}
		if(e.getSource()==newacc)
		{
			newAcc();
			//lb.setText("New Account Registration is Going on...");
		}

		if(e.getSource()==withdraw)
		{
			new Withdraw(frmacc,lb);
		}

		if(e.getSource()==deposit)
		{
			new Deposit(frmacc,lb);
		}

		if(e.getSource()==search)
		{
			new Search(frmacc,lb);
		}

		if(e.getSource()==searchac)
		{
			new Search(frmacc,lb);
		}

		if(e.getSource()==view)
		{
			try {
				view();
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
		}

		if(e.getSource()==exit)
		{
			System.exit(0);
		}

		if(e.getSource()==exitac)
		{
			System.exit(0);
		}

		if(e.getSource()==btacc)
		{
			accCreate();
			frmacc.dispose();
			lb.setText("New Account Registration is Completed.");
		}



	}


	private void view() throws IOException {
		// TODO Auto-generated method stub

		frmv=new JFrame("#Customer Records#");
		frmv.setSize(600,350);
		frmv.setVisible(true);
		pnlv=new JPanel(new BorderLayout());
		frmv.add(pnlv);

		int i=0;
		String data[][]=new String[100][100];
		String col[]={"ACCNo","Name","Balence","Type"};
		Boolean eof=false;
		try {
			din=new DataInputStream(new FileInputStream("BankSystem.txt"));

			while(!eof)
			{
				try{
					while(true)
					{
						for(int j=0;j<=3;j++)
						{
							data[i][j]=din.readUTF();
						}
						i++;
					}

				}catch(EOFException e)
				{
					eof=true;
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}

			din.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		tbv=new JTable(data,col);
		sp=new JScrollPane(tbv);
		pnlv.add(sp);

		lb.setText("Customer Records...");
	}



	private void newAcc() {
		// TODO Auto-generated method stub
		frmacc=new JFrame("New Account");
		frmacc.setSize(450,150);
		frmacc.setVisible(true);
		pnlacc=new JPanel(new FlowLayout());
		frmacc.add(pnlacc);
		pnlacc.add(new JLabel("Name:"));
		tfn=new JTextField(8);
		pnlacc.add(tfn);
		pnlacc.add(new JLabel("Balence:"));
		tfb=new JTextField(8);
		pnlacc.add(tfb);
		pnlacc.add(new JLabel("Type:"));
		tft=new JTextField(8);
		pnlacc.add(tft);

		btacc=new JButton("Ok");
		pnlacc.add(btacc);

		btacc.addActionListener(this);
		lb.setText("New Account Registration is Going on...");

	}

	private void accCreate() {
		// TODO Auto-generated method stub
		try {
			file=new RandomAccessFile("BankSystem.txt","rw");
			file.seek(file.length());
			//			String acc=tfacc.getText();
			int accno=(int)(Math.random()*10000);
			String acc=Integer.toString(accno);
			String name=tfn.getText();
			String bal=tfb.getText();
			String ty=tft.getText();
			if(ty.equals("Savings"))
			{
				if(Double.parseDouble(bal)>2000){
					file.writeUTF(acc);
					file.writeUTF(name);
					file.writeUTF(bal);
					file.writeUTF(ty);
					JOptionPane.showMessageDialog(frmacc, "AccountNo: "+acc+" is Registered");

				}
				else
				{
					JOptionPane.showMessageDialog(frmacc, "Min Balence must be 2000");
				}

			}
			else if(ty.equals("Current"))
			{
				if(Double.parseDouble(bal)>5000){
					file.writeUTF(acc);
					file.writeUTF(name);
					file.writeUTF(bal);
					file.writeUTF(ty);
					JOptionPane.showMessageDialog(frmacc, "AccountNo: "+acc+" is Registered");
				}
				else
				{
					JOptionPane.showMessageDialog(frmacc, "Min Balence must be 5000");
				}

			}
			else
			{
				JOptionPane.showMessageDialog(frmacc, "Invalid Account Type");
			}


		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}


public class BankSys {
	/**
	 * @param args
	 * @author Shantanu 
	 */
	
	JFrame f;
	public static void main(String[] args) throws IOException
	{
		SwingUtilities.invokeLater(new Runnable(){
			public void run()
			{
				new BankSystemPvt();
			}
		});
	}
}

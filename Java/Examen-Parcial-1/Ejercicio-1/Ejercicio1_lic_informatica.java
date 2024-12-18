
import javax.swing.JOptionPane;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */

/**
 *
 * @author Albert Contreras
 */
public class Ejercicio1_lic_informatica extends javax.swing.JFrame {

    /**
     * Creates new form Ejercicio1_lic_informatica
     */
    public Ejercicio1_lic_informatica() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        letrero1 = new javax.swing.JLabel();
        rangoCampo = new javax.swing.JTextField();
        botonImprimir = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Licenciatura en inform�tica");
        setResizable(false);

        letrero1.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        letrero1.setText("Ingrese hasta que n�mero imprimir: ");

        botonImprimir.setText("Imprimir");
        botonImprimir.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                botonImprimirMouseClicked(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(36, 36, 36)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(botonImprimir)
                    .addComponent(letrero1))
                .addGap(18, 18, 18)
                .addComponent(rangoCampo, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(46, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap(30, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(letrero1)
                    .addComponent(rangoCampo, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addComponent(botonImprimir)
                .addContainerGap(28, Short.MAX_VALUE))
        );

        pack();
        setLocationRelativeTo(null);
    }// </editor-fold>//GEN-END:initComponents

    private void botonImprimirMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_botonImprimirMouseClicked
        try {
            int rango = Integer.parseInt(rangoCampo.getText());
            int i = 1;
            var texto = "";
            
            while (i <= rango){
                if(i % 3 == 0 && i % 5 == 0){
                    texto += "Licenciatura en inform�tica\n";
                }else{
                    if(i % 3 == 0){
                        texto += "Licenciatura, ";
                    }else{
                        if(i % 5 == 0){
                            texto += "Inform�tica, ";
                        }else{
                            texto += i + " ";
                        }
                    }
                }
                i++;
                
            }
            
            JOptionPane.showMessageDialog(null, texto);
            rangoCampo.setText("");
            
        } catch (Exception e){
            rangoCampo.setText("");
            JOptionPane.showMessageDialog(null,"Ingrese un n�mero", "Error",JOptionPane.WARNING_MESSAGE);
        }
    }//GEN-LAST:event_botonImprimirMouseClicked

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Ejercicio1_lic_informatica.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Ejercicio1_lic_informatica.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Ejercicio1_lic_informatica.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Ejercicio1_lic_informatica.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Ejercicio1_lic_informatica().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton botonImprimir;
    private javax.swing.JLabel letrero1;
    private javax.swing.JTextField rangoCampo;
    // End of variables declaration//GEN-END:variables
}

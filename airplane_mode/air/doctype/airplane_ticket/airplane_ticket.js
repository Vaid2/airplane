// Copyright (c) 2024, vaibhav and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        if (frm.doc.__islocal) {
            frm.add_custom_button("Assign Seat", () => {
                const seatNumber = prompt('Seat Number');
                if (seatNumber !== null) {
                    frm.set_value("seat", seatNumber);
                    frm.save();
                }
            }, "Actions");
        }
    }
});

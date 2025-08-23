module CIRCUITO3(
  addr,
  data_out
);

  parameter ADDR_WIDTH = 2;
  parameter DATA_WIDTH = 3;

  input  [ADDR_WIDTH-1:0] addr;
  output [DATA_WIDTH-1:0] data_out;
  reg    [DATA_WIDTH-1:0] data_out;

  always @(*) begin
    case(addr)
      2'b00: data_out = 3'b011;
      2'b01: data_out = 3'b110;
      2'b10: data_out = 3'b100;
      2'b11: data_out = 3'b010;
      default: data_out = 3'b000;  // boa prática
    endcase
  end

endmodule

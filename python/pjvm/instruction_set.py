#!/usr/bin/env python
# -*- coding: utf-8 -*-

def nop(code, pc):
    return pc


def bipush(code, pc):
    # 补码处理
    short = code[pc]
    pc += 1

    if short >= 128:
        short -= 256
        # 之前的傻X方法
        # tab = string.maketrans("01", "10")
        # short = -(int(bin(short)[2:].translate(tab), 2) + 1)
    vm_stack.push(short)
    return pc


def sipush(code, pc):
    short1 = code[pc]
    short2 = code[pc + 1]
    pc += 2

    i = short1 << 8 | short2
    if i >= 32768:
        i -= 65536
    vm_stack.push(i)


def return_void(code, pc):
    # TODO
    print "return..."
    pass


def putstatic(code, pc):
    # TODO
    indexbyte1 = code[pc]
    indexbyte2 = code[pc+1]
    pc += 2

    index = (indexbyte1 << 8) | indexbyte2
    value = vm_stack.pop()
    print "Put static: ", index, '=', value


def invokestatic(vm_stack, index):
    pass


def aconst_null(code, pc):
    pass

instruction_call_table = {
    0x00: nop,
    0x01: aconst_null,
    0x02: iconst_m1,
    0x03: iconst_0,
    0x04: iconst_1,
    0x05: iconst_2,
    0x06: iconst_3,
    0x07: iconst_4,
    0x08: iconst_5,
    0x09: lconst_0,
    0x10: lconst_1,
    0x0B: fconst_0,
    0x0C: fconst_1,
    0x0D: fconst_2,
    0x0E: dconst_0,
    0x0F: dconst_1,
    0x10: bipush,
    0x11: sipush,
    0x12: ldc,
    0x13: ldc_w,
    0x14: ldc2_w,
    0x15: iload,
    0x16: lload,
    0x17: fload,
    0x18: dload,
    0x19: aload,
    0x1A: iload_0,
    0x1B: iload_1,
    0x1C: iload_2,
    0x1D: iload_3,
    0x1E: lload_0,
    0x1F: lload_1,
    0x20: lload_2,
    0x21: lload_3,
    0x22: fload_0,
    0x23: fload_1,
    0x24: fload_2,
    0x25: fload_3,
    0x26: dload_0,
    0x27: dload_1,
    0x28: dload_2,
    0x29: dload_3,
    0x2A: aload_0,
    0x2B: aload_1,
    0x2C: aload_2,
    0x2D: aload_3,
    0x2E: iaload,
    0x2F: laload,
    0x30: faload,
    0x31: daload,
    0x32: aaload,
    0x33: baload,
    0x34: caload,
    0x35: saload,
    0x36: istore,
    0x37: lstore,
    0x38: fstore,
    0x39: dstore,
    0x3A: astore,
    0x3B: istore_0,
    0x3C: istore_1,
    0x3D: istore_2,
    0x3E: istore_3,
    0x3F: lstore_0,
    0x40: lstore_1,
    0x41: lstore_2,
    0x42: lstore_3,
    0x43: fstore_0,
    0x44: fstore_1,
    0x45: fstore_2,
    0x46: fstore_3,
    0x47: dstore_0,
    0x48: dstore_1,
    0x49: dstore_2,
    0x4A: dstore_3,
    0x4B: astore_0,
    0x4C: astore_1,
    0x4D: astore_2,
    0x4E: astore_3,
    0x4F: iastore,
    0x50: lastore,
    0x51: fastore,
    0x52: dastore,
    0x53: aastore,
    0x54: bastore,
    0x55: castore,
    0x56: sastore,
    0x57: pop,
    0x58: pop2,
    0x59: dup,
    0x5A: dup_x1,
    0x5B: dup_x2,
    0x5C: dup2,
    0x5D: dup2_x1,
    0x5E: dup2_x2,
    0x5F: swap,
    0x60: iadd,
    0x61: ladd,
    0x62: fadd,
    0x63: dadd,
    0x64: isub,
    0x65: lsub,
    0x66: fsub,
    0x67: dsub,
    0x68: imul,
    0x69: lmul,
    0x6A: fmul,
    0x6B: dmul,
    0x6C: idiv,
    0x6D: ldiv,
    0x6E: fdiv,
    0x6F: ddiv,
    0x70: irem,
    0x71: lrem,
    0x72: frem,
    0x73: drem,
    0x74: ineg,
    0x75: lneg,
    0x76: fneg,
    0x77: dneg,
    0x78: ishl,
    0x79: lshl,
    0x7A: ishr,
    0x7B: lshr,
    0x7C: iushr,
    0x7B: lushr,
    0x7E: iand,
    0x7F: land,
    0x80: ior,
    0x81: lor,
    0x82: ixor,
    0x83: lxor,
    0x84: iinc,
    0x85: i2l,
    0x86: i2f,
    0x87: i2d,
    0x88: l2f,
    0x89: l2f,
    0x8A: l2d,
    0x8B: f2i,
    0x8C: f2l,
    0x8D: f2d,
    0x8E: d2i,
    0x8F: d2l,
    0x90: d2f,
    0x91: i2b,
    0x92: i2c,
    0x93: i2s,
    0x94: lcmp,
    0x95: fcmpl,
    0x96: fcmpg,
    0x97: dcmpl,
    0x98: dcmpg,
    0x99: ifeq,
    0x9A: ifne,
    0x9B: iflt,
    0x9C: ifge,
    0x9D: ifgt,
    0x9E: ifle,
    0x9F: if_icmpeq,
    0xA0: if_acmpne,
    0xA1: if_icmplt,
    0xA2: if_icmpge,
    0xA3: if_icmpgt,
    0xA4: if_icmple,
    0xA5: if_acmpeq,
    0xA6: if_acmpne,
    0xA7: goto,
    0xA8: jsr,
    0xA9: ret,
    0xAA: tableswitch,
    0xAB: lookupswitch,
    0xAC: ireturn,
    0xAD: lreturn,
    0xAE: freturn,
    0xAF: dreturn,
    0xB0: areturn,
    0xB1: return_void,
    0xB2: getstatic,
    0xB3: putstatic,
    0xB4: getfield,
    0xB5: putfield,
    0xB6: invokevirtual,
    0xB7: invokespecial,
    0xB8: invokestatic,
    0xB9: invokeinterface,
    0xBA: invokedynamic,
    0xBB: new,
    0xBC: newarray,
    0xBD: anewarray,
    0xBE: arraylength,
    0xBF: athrow,
    0xC0: checkcast,
    0xC1: instanceof,
    0xC2: monitorenter,
    0xC3: monitorexit,
    0xC4: wide,
    0xC5: multianewarray,
    0xC6: ifnull,
    0xC7: ifnonnull,
    0xC8: goto_w,
    0xC9: jsr_w,
    0xCA: breakpoint,
    0xFE: impdep1,
    0xFF: impdep2,
    }



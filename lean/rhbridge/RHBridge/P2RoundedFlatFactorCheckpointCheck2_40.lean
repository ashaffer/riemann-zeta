import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel2FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel2FlatComponentChunk40

end RHP2Bridge

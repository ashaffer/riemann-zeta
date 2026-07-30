import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel1FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel1FlatComponentChunk40

end RHP2Bridge

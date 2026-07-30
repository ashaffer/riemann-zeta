import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel1FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel1FlatComponentChunk24

end RHP2Bridge

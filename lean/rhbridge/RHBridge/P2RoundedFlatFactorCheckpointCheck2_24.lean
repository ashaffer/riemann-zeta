import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel2FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel2FlatComponentChunk24

end RHP2Bridge

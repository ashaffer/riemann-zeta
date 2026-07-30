import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel2FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel2FlatComponentChunk27

end RHP2Bridge

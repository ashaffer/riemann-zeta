import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel2FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel2FlatComponentChunk34

end RHP2Bridge

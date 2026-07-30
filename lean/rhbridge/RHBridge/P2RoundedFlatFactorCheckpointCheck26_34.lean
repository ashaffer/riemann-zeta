import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel26FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel26FlatComponentChunk34

end RHP2Bridge

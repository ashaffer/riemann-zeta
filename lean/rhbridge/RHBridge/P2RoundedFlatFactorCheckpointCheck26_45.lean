import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel26FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel26FlatComponentChunk45

end RHP2Bridge

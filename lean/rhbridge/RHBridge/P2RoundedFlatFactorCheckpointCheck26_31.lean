import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel26FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel26FlatComponentChunk31

end RHP2Bridge

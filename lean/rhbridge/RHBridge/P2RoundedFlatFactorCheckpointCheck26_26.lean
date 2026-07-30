import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel26FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel26FlatComponentChunk26

end RHP2Bridge

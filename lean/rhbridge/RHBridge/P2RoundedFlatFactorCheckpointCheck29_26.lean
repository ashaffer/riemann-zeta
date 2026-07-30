import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel29FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel29FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel29FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel29FlatComponentChunk26

end RHP2Bridge

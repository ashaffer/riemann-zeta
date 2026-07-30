import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk2 :
    P2RoundedFactorCheckpointData.panel29FlatEven2 =
      (P2RoundedFactorCheckpointData.panel29TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel29FlatEven2_eq :
    P2RoundedFactorCheckpointData.panel29FlatEven2 =
      (P2RoundedFactorCheckpointData.panel29TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  exact panel29FlatComponentChunk2

end RHP2Bridge

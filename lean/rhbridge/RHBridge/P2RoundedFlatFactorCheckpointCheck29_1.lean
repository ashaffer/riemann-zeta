import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk1 :
    P2RoundedFactorCheckpointData.panel29FlatEven1 =
      (P2RoundedFactorCheckpointData.panel29TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel29FlatEven1_eq :
    P2RoundedFactorCheckpointData.panel29FlatEven1 =
      (P2RoundedFactorCheckpointData.panel29TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  exact panel29FlatComponentChunk1

end RHP2Bridge

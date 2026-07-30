import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk3 :
    P2RoundedFactorCheckpointData.panel8FlatEven3 =
      (P2RoundedFactorCheckpointData.panel8TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel8FlatEven3_eq :
    P2RoundedFactorCheckpointData.panel8FlatEven3 =
      (P2RoundedFactorCheckpointData.panel8TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  exact panel8FlatComponentChunk3

end RHP2Bridge

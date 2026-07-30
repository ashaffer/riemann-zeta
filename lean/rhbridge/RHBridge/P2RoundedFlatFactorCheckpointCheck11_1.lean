import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk1 :
    P2RoundedFactorCheckpointData.panel11FlatEven1 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel11FlatEven1_eq :
    P2RoundedFactorCheckpointData.panel11FlatEven1 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  exact panel11FlatComponentChunk1

end RHP2Bridge

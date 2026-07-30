import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk14 :
    P2RoundedFactorCheckpointData.panel11FlatEven14 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel11FlatEven14_eq :
    P2RoundedFactorCheckpointData.panel11FlatEven14 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  exact panel11FlatComponentChunk14

end RHP2Bridge

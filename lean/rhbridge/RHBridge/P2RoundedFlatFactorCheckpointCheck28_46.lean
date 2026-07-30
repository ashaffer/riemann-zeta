import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel28FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel28FlatComponentChunk46

end RHP2Bridge

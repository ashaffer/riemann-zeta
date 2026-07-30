import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk15 :
    P2RoundedFactorCheckpointData.panel25Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix60_eq :
    P2RoundedFactorCheckpointData.panel25Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk15.1

theorem panel25Prefix61_eq :
    P2RoundedFactorCheckpointData.panel25Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk15.2.1

theorem panel25Prefix62_eq :
    P2RoundedFactorCheckpointData.panel25Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk15.2.2.1

theorem panel25Prefix63_eq :
    P2RoundedFactorCheckpointData.panel25Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk15.2.2.2

end RHP2Bridge

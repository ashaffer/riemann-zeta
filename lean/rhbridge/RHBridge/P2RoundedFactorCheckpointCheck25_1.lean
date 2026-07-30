import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk1 :
    P2RoundedFactorCheckpointData.panel25Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix4_eq :
    P2RoundedFactorCheckpointData.panel25Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk1.1

theorem panel25Prefix5_eq :
    P2RoundedFactorCheckpointData.panel25Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk1.2.1

theorem panel25Prefix6_eq :
    P2RoundedFactorCheckpointData.panel25Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk1.2.2.1

theorem panel25Prefix7_eq :
    P2RoundedFactorCheckpointData.panel25Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk1.2.2.2

end RHP2Bridge

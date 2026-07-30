import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk1 :
    P2RoundedFactorCheckpointData.panel22Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix4_eq :
    P2RoundedFactorCheckpointData.panel22Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk1.1

theorem panel22Prefix5_eq :
    P2RoundedFactorCheckpointData.panel22Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk1.2.1

theorem panel22Prefix6_eq :
    P2RoundedFactorCheckpointData.panel22Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk1.2.2.1

theorem panel22Prefix7_eq :
    P2RoundedFactorCheckpointData.panel22Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk1.2.2.2

end RHP2Bridge

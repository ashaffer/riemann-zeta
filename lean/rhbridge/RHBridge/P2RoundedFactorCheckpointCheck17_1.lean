import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk1 :
    P2RoundedFactorCheckpointData.panel17Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix4_eq :
    P2RoundedFactorCheckpointData.panel17Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk1.1

theorem panel17Prefix5_eq :
    P2RoundedFactorCheckpointData.panel17Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk1.2.1

theorem panel17Prefix6_eq :
    P2RoundedFactorCheckpointData.panel17Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk1.2.2.1

theorem panel17Prefix7_eq :
    P2RoundedFactorCheckpointData.panel17Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk1.2.2.2

end RHP2Bridge

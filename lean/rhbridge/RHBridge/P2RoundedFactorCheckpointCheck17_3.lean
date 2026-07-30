import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk3 :
    P2RoundedFactorCheckpointData.panel17Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix12_eq :
    P2RoundedFactorCheckpointData.panel17Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk3.1

theorem panel17Prefix13_eq :
    P2RoundedFactorCheckpointData.panel17Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk3.2.1

theorem panel17Prefix14_eq :
    P2RoundedFactorCheckpointData.panel17Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk3.2.2.1

theorem panel17Prefix15_eq :
    P2RoundedFactorCheckpointData.panel17Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk3.2.2.2

end RHP2Bridge

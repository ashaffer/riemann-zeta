import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk4 :
    P2RoundedFactorCheckpointData.panel15Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix16_eq :
    P2RoundedFactorCheckpointData.panel15Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk4.1

theorem panel15Prefix17_eq :
    P2RoundedFactorCheckpointData.panel15Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk4.2.1

theorem panel15Prefix18_eq :
    P2RoundedFactorCheckpointData.panel15Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk4.2.2.1

theorem panel15Prefix19_eq :
    P2RoundedFactorCheckpointData.panel15Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk4.2.2.2

end RHP2Bridge
